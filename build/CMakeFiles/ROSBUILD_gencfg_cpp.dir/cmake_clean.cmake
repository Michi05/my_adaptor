FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "../src/my_adaptor/msg"
  "../src/my_adaptor/srv"
  "CMakeFiles/ROSBUILD_gencfg_cpp"
  "../cfg/cpp/my_adaptor/propertiesConfig.h"
  "../docs/propertiesConfig.dox"
  "../docs/propertiesConfig-usage.dox"
  "../src/my_adaptor/cfg/propertiesConfig.py"
  "../docs/propertiesConfig.wikidoc"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gencfg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
