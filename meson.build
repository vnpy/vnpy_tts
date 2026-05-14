project(
  'vnpy_tts',
  'cpp',
  version: '6.7.2.3',
  license: 'MIT',
  meson_version: '>=1.7.0',
  default_options: [
    'buildtype=release',
    'cpp_std=c++17',
    'warning_level=2',
  ],
)

# 导入文件系统和Python模块
fs = import('fs')
py = import('python').find_installation(pure: false)
py_dep = py.dependency()

# 获取pybind11路径
python_cmd = host_machine.system() == 'windows' ? 'python' : 'python3'
pybind11_include_dir = run_command(python_cmd, '-c', 'import pybind11; print(pybind11.get_include())', check: true).stdout().strip()
message('使用pybind11路径: ' + pybind11_include_dir)

# 获取编译器信息
cpp = meson.get_compiler('cpp')
compiler_id = cpp.get_id()

# 输出构建目标系统信息
message('构建目标系统: ' + host_machine.system())

# 初始化变量
thostmduserapi_lib = []
thosttraderapi_lib = []
extra_cpp_args = []
extra_link_args = []

# 初始化库变量
thostmduserapi_lib = []
thosttraderapi_lib = []

# 初始化其他编译选项
extra_link_args = []
install_rpath_value = ''

# 设置Windows特定编译选项
if host_machine.system() == 'windows'
  # Windows编译器设置
  add_project_arguments('/MT', language : 'cpp')
  
  # 设置库目录
  lib_dir = meson.current_source_dir() / 'vnpy_tts/api/libs'
  api_dir = meson.current_source_dir() / 'vnpy_tts/api'
  
  # 设置include目录
  include_dirs = include_directories(
    'vnpy_tts/api/include',
    'vnpy_tts/api/vntts',
    pybind11_include_dir,
  )
  
  # 定义CTP库
  thostmduserapi_lib = cpp.find_library('thostmduserapi_se', 
                                       dirs: [lib_dir, api_dir],
                                       required: true)
  thosttraderapi_lib = cpp.find_library('thosttraderapi_se', 
                                       dirs: [lib_dir, api_dir],
                                       required: true)

# 设置Mac特定编译选项
elif host_machine.system() == 'darwin'
  # Mac编译器设置
  extra_cpp_args = [
    '-std=c++11',
    '-mmacosx-version-min=10.12',
  ]

  extra_link_args = [
    '-mmacosx-version-min=10.12',
  ]

  install_rpath_value = '@loader_path'

  # 设置库目录
  lib_dir = meson.current_source_dir() / 'vnpy_tts/api/libs'
  api_dir = meson.current_source_dir() / 'vnpy_tts/api'

  # 设置include目录（优先使用Mac专用头文件目录）
  include_dir_value = fs.is_dir('vnpy_tts/api/include/mac') ? 'vnpy_tts/api/include/mac' : 'vnpy_tts/api/include'
  include_dirs = include_directories(
    include_dir_value,
    'vnpy_tts/api/vntts',
    pybind11_include_dir,
  )

  # 优先使用framework结构（若存在），否则回退为dylib/lib方式
  if fs.is_dir('vnpy_tts/api/thostmduserapi_se.framework')
    thostmduserapi_lib = declare_dependency(
      dependencies: [py_dep],
      link_args: [
        '-F', api_dir,
        '-framework', 'thostmduserapi_se'
      ]
    )
  else
    thostmduserapi_lib = cpp.find_library('thostmduserapi_se',
                                         dirs: [api_dir, lib_dir],
                                         required: true)
  endif

  if fs.is_dir('vnpy_tts/api/thosttraderapi_se.framework')
    thosttraderapi_lib = declare_dependency(
      dependencies: [py_dep],
      link_args: [
        '-F', api_dir,
        '-framework', 'thosttraderapi_se'
      ]
    )
  else
    thosttraderapi_lib = cpp.find_library('thosttraderapi_se',
                                         dirs: [api_dir, lib_dir],
                                         required: true)
  endif

# 设置Linux特定编译选项
else  # Linux
  # Linux编译器设置
  extra_cpp_args = [
    '-std=c++17',
    '-O3',
    '-Wno-delete-incomplete',
    '-Wno-sign-compare',
  ]
  
  extra_link_args = [
    '-lstdc++',
  ]

  install_rpath_value = '$ORIGIN'
  
  # 设置库目录
  lib_dir = meson.current_source_dir() / 'vnpy_tts/api'
  
  # 设置include目录
  include_dirs = include_directories(
    'vnpy_tts/api/include',
    'vnpy_tts/api/vntts',
    pybind11_include_dir,
  )
  
  # 定义CTP库
  thostmduserapi_lib = cpp.find_library('thostmduserapi_se', 
                                       dirs: [lib_dir],
                                       required: true)
  thosttraderapi_lib = cpp.find_library('thosttraderapi_se', 
                                       dirs: [lib_dir],
                                       required: true)
endif

# 创建MD模块扩展
md_module = py.extension_module(
  'vnttsmd',
  sources: ['vnpy_tts/api/vntts/vnttsmd/vnttsmd.cpp'],
  include_directories: include_dirs,
  dependencies: [py_dep, thostmduserapi_lib],
  cpp_args: extra_cpp_args,
  link_args: extra_link_args,
  install: true,
  install_rpath: install_rpath_value,
  subdir: 'vnpy_tts/api'
)

# 创建TD模块扩展
td_module = py.extension_module(
  'vnttstd',
  sources: ['vnpy_tts/api/vntts/vnttstd/vnttstd.cpp'],
  include_directories: include_dirs,
  dependencies: [py_dep, thosttraderapi_lib],
  cpp_args: extra_cpp_args,
  link_args: extra_link_args,
  install: true,
  install_rpath: install_rpath_value,
  subdir: 'vnpy_tts/api'
)

# 安装Python源代码
python_files = [
  ['vnpy_tts/__init__.py', 'vnpy_tts'],
  ['vnpy_tts/api/__init__.py', 'vnpy_tts/api'],
  ['vnpy_tts/api/tts_constant.py', 'vnpy_tts/api'],
  ['vnpy_tts/gateway/__init__.py', 'vnpy_tts/gateway'],
  ['vnpy_tts/gateway/tts_gateway.py', 'vnpy_tts/gateway'],
]

foreach file : python_files
  py.install_sources(
    [file[0]],
    pure: false,
    subdir: file[1]
  )
endforeach

# 安装API动态库文件
if host_machine.system() == 'windows'
  api_libs = [
    'vnpy_tts/api/thostmduserapi_se.dll',
    'vnpy_tts/api/thosttraderapi_se.dll',
  ]
  
  install_data(
    api_libs,
    install_dir: py.get_install_dir() / 'vnpy_tts/api'
  )
elif host_machine.system() == 'darwin'
  # 安装Mac Framework文件夹（如存在）
  if fs.is_dir('vnpy_tts/api/thostmduserapi_se.framework')
    install_subdir(
      'vnpy_tts/api/thostmduserapi_se.framework',
      install_dir: py.get_install_dir() / 'vnpy_tts/api'
    )
  endif

  if fs.is_dir('vnpy_tts/api/thosttraderapi_se.framework')
    install_subdir(
      'vnpy_tts/api/thosttraderapi_se.framework',
      install_dir: py.get_install_dir() / 'vnpy_tts/api'
    )
  endif

  # 安装dylib（如存在）
  api_dylibs = []
  if fs.exists('vnpy_tts/api/libthostmduserapi_se.dylib')
    api_dylibs += ['vnpy_tts/api/libthostmduserapi_se.dylib']
  endif
  if fs.exists('vnpy_tts/api/libthosttraderapi_se.dylib')
    api_dylibs += ['vnpy_tts/api/libthosttraderapi_se.dylib']
  endif
  if api_dylibs.length() > 0
    install_data(
      api_dylibs,
      install_dir: py.get_install_dir() / 'vnpy_tts/api'
    )
  endif
else  # Linux
  api_libs = [
    'vnpy_tts/api/libthostmduserapi_se.so',
    'vnpy_tts/api/libthosttraderapi_se.so',
  ]
  
  install_data(
    api_libs,
    install_dir: py.get_install_dir() / 'vnpy_tts/api'
  )
endif
