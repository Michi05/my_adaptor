FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "../src/my_adaptor/msg"
  "../src/my_adaptor/srv"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/my_adaptor/srv/__init__.py"
  "../src/my_adaptor/srv/_booleanValue.py"
  "../src/my_adaptor/srv/_floatValue.py"
  "../src/my_adaptor/srv/_disparityImage.py"
  "../src/my_adaptor/srv/_setFloat.py"
  "../src/my_adaptor/srv/_intValue.py"
  "../src/my_adaptor/srv/_setInteger.py"
  "../src/my_adaptor/srv/_setString.py"
  "../src/my_adaptor/srv/_requestTopic.py"
  "../src/my_adaptor/srv/_stringValue.py"
  "../src/my_adaptor/srv/_setBoolean.py"
  "../src/my_adaptor/srv/_normalImage.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
