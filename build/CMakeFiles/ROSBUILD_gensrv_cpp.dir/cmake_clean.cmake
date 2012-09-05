FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "../src/my_adaptor/msg"
  "../src/my_adaptor/srv"
  "CMakeFiles/ROSBUILD_gensrv_cpp"
  "../srv_gen/cpp/include/my_adaptor/booleanValue.h"
  "../srv_gen/cpp/include/my_adaptor/floatValue.h"
  "../srv_gen/cpp/include/my_adaptor/disparityImage.h"
  "../srv_gen/cpp/include/my_adaptor/setFloat.h"
  "../srv_gen/cpp/include/my_adaptor/intValue.h"
  "../srv_gen/cpp/include/my_adaptor/setInteger.h"
  "../srv_gen/cpp/include/my_adaptor/setString.h"
  "../srv_gen/cpp/include/my_adaptor/requestTopic.h"
  "../srv_gen/cpp/include/my_adaptor/stringValue.h"
  "../srv_gen/cpp/include/my_adaptor/setBoolean.h"
  "../srv_gen/cpp/include/my_adaptor/normalImage.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
