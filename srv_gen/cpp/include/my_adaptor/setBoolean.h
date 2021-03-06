/* Auto-generated by genmsg_cpp for file /home/r00t/ros_workspace/my_adaptor/srv/setBoolean.srv */
#ifndef MY_ADAPTOR_SERVICE_SETBOOLEAN_H
#define MY_ADAPTOR_SERVICE_SETBOOLEAN_H
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
struct setBooleanRequest_ {
  typedef setBooleanRequest_<ContainerAllocator> Type;

  setBooleanRequest_()
  : topicName()
  , newValue(false)
  {
  }

  setBooleanRequest_(const ContainerAllocator& _alloc)
  : topicName(_alloc)
  , newValue(false)
  {
  }

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _topicName_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  topicName;

  typedef uint8_t _newValue_type;
  uint8_t newValue;


  typedef boost::shared_ptr< ::my_adaptor::setBooleanRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::my_adaptor::setBooleanRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct setBooleanRequest
typedef  ::my_adaptor::setBooleanRequest_<std::allocator<void> > setBooleanRequest;

typedef boost::shared_ptr< ::my_adaptor::setBooleanRequest> setBooleanRequestPtr;
typedef boost::shared_ptr< ::my_adaptor::setBooleanRequest const> setBooleanRequestConstPtr;


template <class ContainerAllocator>
struct setBooleanResponse_ {
  typedef setBooleanResponse_<ContainerAllocator> Type;

  setBooleanResponse_()
  : setAnswer(false)
  {
  }

  setBooleanResponse_(const ContainerAllocator& _alloc)
  : setAnswer(false)
  {
  }

  typedef uint8_t _setAnswer_type;
  uint8_t setAnswer;


  typedef boost::shared_ptr< ::my_adaptor::setBooleanResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::my_adaptor::setBooleanResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct setBooleanResponse
typedef  ::my_adaptor::setBooleanResponse_<std::allocator<void> > setBooleanResponse;

typedef boost::shared_ptr< ::my_adaptor::setBooleanResponse> setBooleanResponsePtr;
typedef boost::shared_ptr< ::my_adaptor::setBooleanResponse const> setBooleanResponseConstPtr;

struct setBoolean
{

typedef setBooleanRequest Request;
typedef setBooleanResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct setBoolean
} // namespace my_adaptor

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::my_adaptor::setBooleanRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::my_adaptor::setBooleanRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::my_adaptor::setBooleanRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "ea7f36159508c763698feeeea10ee2bc";
  }

  static const char* value(const  ::my_adaptor::setBooleanRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xea7f36159508c763ULL;
  static const uint64_t static_value2 = 0x698feeeea10ee2bcULL;
};

template<class ContainerAllocator>
struct DataType< ::my_adaptor::setBooleanRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "my_adaptor/setBooleanRequest";
  }

  static const char* value(const  ::my_adaptor::setBooleanRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::my_adaptor::setBooleanRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "string topicName\n\
bool newValue\n\
\n\
";
  }

  static const char* value(const  ::my_adaptor::setBooleanRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::my_adaptor::setBooleanResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::my_adaptor::setBooleanResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::my_adaptor::setBooleanResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "e630a2f2cea41edbedb990c35c6910ef";
  }

  static const char* value(const  ::my_adaptor::setBooleanResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xe630a2f2cea41edbULL;
  static const uint64_t static_value2 = 0xedb990c35c6910efULL;
};

template<class ContainerAllocator>
struct DataType< ::my_adaptor::setBooleanResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "my_adaptor/setBooleanResponse";
  }

  static const char* value(const  ::my_adaptor::setBooleanResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::my_adaptor::setBooleanResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool setAnswer\n\
\n\
\n\
";
  }

  static const char* value(const  ::my_adaptor::setBooleanResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::my_adaptor::setBooleanResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::my_adaptor::setBooleanRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.topicName);
    stream.next(m.newValue);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct setBooleanRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::my_adaptor::setBooleanResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.setAnswer);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct setBooleanResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<my_adaptor::setBoolean> {
  static const char* value() 
  {
    return "fde587b1db6e33328e50f2ea2c9e870b";
  }

  static const char* value(const my_adaptor::setBoolean&) { return value(); } 
};

template<>
struct DataType<my_adaptor::setBoolean> {
  static const char* value() 
  {
    return "my_adaptor/setBoolean";
  }

  static const char* value(const my_adaptor::setBoolean&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<my_adaptor::setBooleanRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "fde587b1db6e33328e50f2ea2c9e870b";
  }

  static const char* value(const my_adaptor::setBooleanRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<my_adaptor::setBooleanRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "my_adaptor/setBoolean";
  }

  static const char* value(const my_adaptor::setBooleanRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<my_adaptor::setBooleanResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "fde587b1db6e33328e50f2ea2c9e870b";
  }

  static const char* value(const my_adaptor::setBooleanResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<my_adaptor::setBooleanResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "my_adaptor/setBoolean";
  }

  static const char* value(const my_adaptor::setBooleanResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // MY_ADAPTOR_SERVICE_SETBOOLEAN_H

