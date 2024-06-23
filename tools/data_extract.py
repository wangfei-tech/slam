import rosbag
from sensor_msgs.msg import LaserScan
import rospy
# 输入的bag文件路径
bag_file = '/home/wf/HUASHINE/data/2024-05-22-11-00-34.bag'

# 输出的文本文件路径
output_file = 'file.txt'
recording_started = False
# 要读取的topic名称
topic_name = '/scan'

# 打开bag文件
bag = rosbag.Bag(bag_file, 'r')

# 打开输出文件
with open(output_file, 'w') as f:
    # 遍历bag文件中的每一条消息
    for topic, msg, t in bag.read_messages(topics=[topic_name]):
        timestamp = msg.header.stamp.to_sec()
        # print(timestamp)
    # 如果时间戳大于等于60秒，则开始记录数据
        if timestamp >= 0.0:
            rospy.loginfo("Started recording data at timestamp %.2f", timestamp)
        # 检查消息类型是否为LaserScan
        # 写入'laser'到文件
            f.write("laser ")
        # 写入ranges数据到文件
            print(len(msg.ranges))
            for range_value in msg.ranges:
                f.write(str(range_value) + " ")
            # 换行
            f.write("\n")

# 关闭bag文件
bag.close()

