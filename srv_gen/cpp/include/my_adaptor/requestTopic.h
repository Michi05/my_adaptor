/* Auto-generated by genmsg_cpp for file /home/r00t/ros_workspace/my_adaptor/srv/requestTopic.srv */
#ifndef MY_ADAPTOR_SERVICE_REQUESTTOPIC_H
#define MY_ADAPTOR_SERVICE_REQUESTTOPIC_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "ros/service_traits.h"




namespace my_adaptor
{
template <class ContainerAllocator>
struct requestTopicRequest_ {
  typedef requestTopicRequest_<ContainerAllocator> Type;

  requestTopicRequest_()
  : nImages(0)
  , sourceTopic()
  , responseTopic()
  {
  }

  requestTopicRequest_(const ContainerAllocator& _alloc)
  : nImages(0)
  , sourceTopic(_alloc)
  , responseTopic(_alloc)
  {
  }

  typedef int64_t _nImages_type;
  int64_t nImages;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _sourceTopic_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  sourceTopic;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _responseTopic_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  responseTopic;


  typedef boost::shared_ptr< ::my_adaptor::requestTopicRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::my_adaptor::requestTopicRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct requestTopicRequest
typedef  ::my_adaptor::requestTopicRequest_<std::allocator<void> > requestTopicRequest;

typedef boost::shared_ptr< ::my_adaptor::requestTopicRequest> requestTopicRequestPtr;
typedef boost::shared_ptr< ::my_adaptor::requestTopicRequest const> requestTopicRequestConstPtr;


template <class ContainerAllocator>
struct requestTopicResponse_ {
  typedef requestTopicResponse_<ContainerAllocator> Type;

  requestTopicResponse_()
  : response()
  {
  }

  requestTopicResponse_(const ContainerAllocator& _alloc)
  : response(_alloc)
  {
  }

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _response_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  response;


  typedef boost::shared_ptr< ::my_adaptor::requestTopicResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::my_adaptor::requestTopicResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct requestTopicResponse
typedef  ::my_adaptor::requestTopicResponse_<std::allocator<void> > requestTopicResponse;

typedef boost::shared_ptr< ::my_adaptor::requestTopicResponse> requestTopicResponsePtr;
typedef boost::shared_ptr< ::my_adaptor::requestTopicResponse const> requestTopicResponseConstPtr;

struct requestTopic
{

typedef requestTopicRequest Request;
typedef requestTopicResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct requestTopic
} // namespace my_adaptor

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::my_adaptor::requestTopicRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::my_adaptor::requestTopicRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::my_adaptor::requestTopicRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "649216dbe3b2606914f2eb065f7f6dab";
  }

  static const char* value(const  ::my_adaptor::requestTopicRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x649216dbe3b26069ULL;
  static const uint64_t static_value2 = 0x14f2eb065f7f6dabULL;
};

template<class ContainerAllocator>
struct DataType< ::my_adaptor::requestTopicRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "my_adaptor/requestTopicRequest";
  }

  static const char* value(const  ::my_adaptor::requestTopicRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::my_adaptor::requestTopicRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "int64 nImages\n\
string sourceTopic\n\
string responseTopic\n\
\n\
";
  }

  static const char* value(const  ::my_adaptor::requestTopicRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::my_adaptor::requestTopicResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::my_adaptor::requestTopicResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::my_adaptor::requestTopicResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "6de314e2dc76fbff2b6244a6ad70b68d";
  }

  static const char* value(const  ::my_adaptor::requestTopicResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x6de314e2dc76fbffULL;
  static const uint64_t static_value2 = 0x2b6244a6ad70b68dULL;
};

template<class ContainerAllocator>
struct DataType< ::my_adaptor::requestTopicResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "my_adaptor/requestTopicResponse";
  }

  static const char* value(const  ::my_adaptor::requestTopicResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::my_adaptor::requestTopicResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "string response\n\
\n\
\n\
\n\
";
  }

  static const char* value(const  ::my_adaptor::requestTopicResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::my_adaptor::requestTopicRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.nImages);
    stream.next(m.sourceTopic);
    stream.next(m.responseTopic);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct requestTopicRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::my_adaptor::requestTopicResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.response);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct requestTopicResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<my_adaptor::requestTopic> {
  static const char* value() 
  {
    return "b817ce56db2701eab6ea62d45b0f064b";
  }

  static const char* value(const my_adaptor::requestTopic&) { return value(); } 
};

template<>
struct DataType<my_adaptor::requestTopic> {
  static const char* value() 
  {
    return "my_adaptor/requestTopic";
  }

  static const char* value(const my_adaptor::requestTopic&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<my_adaptor::requestTopicRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b817ce56db2701eab6ea62d45b0f064b";
  }

  static const char* value(const my_adaptor::requestTopicRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<my_adaptor::requestTopicRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "my_adaptor/requestTopic";
  }

  static const char* value(const my_adaptor::requestTopicRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<my_adaptor::requestTopicResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b817ce56db2701eab6ea62d45b0f064b";
  }

  static const char* value(const my_adaptor::requestTopicResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<my_adaptor::requestTopicResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "my_adaptor/requestTopic";
  }

  static const char* value(const my_adaptor::requestTopicResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // MY_ADAPTOR_SERVICE_REQUESTTOPIC_H
