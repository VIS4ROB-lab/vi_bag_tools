import rosbag
import os
import numpy as np
#import sm
#import pylab as pl


class BagOdometryDatasetReaderIterator(object):
    def __init__(self,dataset,indices=None):
        self.dataset = dataset
        if indices is None:
            self.indices = np.arange(dataset.numMessages())
        else:
            self.indices = indices
        self.iter = self.indices.__iter__()
    def __iter__(self):
        return self
    def next(self):
        idx = self.iter.next()
        return self.dataset.getMessage(idx)

class BagOdometryDatasetReader(object):
    def __init__(self, bagfile, odometrytopic, bag_from_to=None):
        self.bagfile = bagfile
        self.topic = odometrytopic
        #self.perform_synchronization = perform_synchronization
        self.bag = rosbag.Bag(bagfile)
        self.uncompress = None
        if odometrytopic is None:
            raise RuntimeError("Please pass in a topic name referring to the odometry stream in the bag file\n{0}".format(self.bag));

        # Get the message indices
        conx = self.bag._get_connections(topics=odometrytopic)
        indices = self.bag._get_indexes(conx)
        
        try:
            self.index = indices.next()
        except:
            raise RuntimeError("Could not find topic {0} in {1}.".format(odometrytopic, self.bagfile))
        
        self.indices = np.arange(len(self.index))
        
        #sort the indices by header.stamp
        self.indices = self.sortByTime(self.indices)
        
        #go through the bag and remove the indices outside the timespan [bag_start_time, bag_end_time]
        if bag_from_to:
            self.indices = self.truncateIndicesFromTime(self.indices, bag_from_to)
            
    #sort the ros messages by the header time not message time
    def sortByTime(self, indices):
    #    self.timestamp_corrector = sm.DoubleTimestampCorrector()
        timestamps=list()
        for idx in self.indices:
            topic, data, stamp = self.bag._read_message(self.index[idx].position)
            timestamp = data.header.stamp.secs*1e9 + data.header.stamp.nsecs
            timestamps.append(timestamp)
        #    if self.perform_synchronization:
        #        self.timestamp_corrector.correctTimestamp(data.header.stamp.to_sec(), \
        #                                                  stamp.to_sec())
        
        sorted_tuples = sorted(zip(timestamps, indices))
        sorted_indices = [tuple_value[1] for tuple_value in sorted_tuples]
        return sorted_indices
    
    def truncateIndicesFromTime(self, indices, bag_from_to):
        #get the timestamps
        timestamps=list()
        for idx in self.indices:
            topic, data, stamp = self.bag._read_message(self.index[idx].position)
            timestamp = data.header.stamp.secs + data.header.stamp.nsecs/1.0e9
            timestamps.append(timestamp)

        bagstart = min(timestamps)
        baglength = max(timestamps)-bagstart
        print "bagstart",bagstart
        print "baglength",baglength
        #some value checking
        if bag_from_to[0]>=bag_from_to[1]:
            raise RuntimeError("Bag start time must be bigger than end time.".format(bag_from_to[0]))
        if bag_from_to[0]<0.0:
            print("Bag start time of {0} s is smaller 0".format(bag_from_to[0]) )
        if bag_from_to[1]>baglength:
            print("Bag end time of {0} s is bigger than the total length of {1} s".format(bag_from_to[1], baglength) )

        #find the valid timestamps
        valid_indices = []
        for idx, timestamp in enumerate(timestamps):
             if timestamp>=(bagstart+bag_from_to[0]) and timestamp<=(bagstart+bag_from_to[1]):
                 valid_indices.append(idx)  
        print("BagImuDatasetReader: truncated {0} / {1} messages.".format(len(indices)-len(valid_indices), len(indices)))
        
        return valid_indices
    
    def __iter__(self):
        # Reset the bag reading
        return self.readDataset()
    
    def readDataset(self):
        return BagOdometryDatasetReaderIterator(self, self.indices)

    def readDatasetShuffle(self):
        indices = self.indices
        np.random.shuffle(indices)
        return BagOdometryDatasetReaderIterator(self,indices)

    def numMessages(self):
        return len(self.indices)
    
    def getMessage(self,idx):
        topic, data, stamp = self.bag._read_message(self.index[idx].position)
        time = data.header.stamp
        seq = data.header.seq
        timestamp = data.header.stamp.to_nsec()
        frame_id = data.header.frame_id
        position = np.array( [data.pose.pose.position.x, data.pose.pose.position.y, data.pose.pose.position.z] )
        orientation = np.array( [data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w] )       
        return (time, seq, timestamp, frame_id, position, orientation)
