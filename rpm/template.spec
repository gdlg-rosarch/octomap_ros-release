Name:           ros-jade-octomap-ros
Version:        0.4.0
Release:        1%{?dist}
Summary:        ROS octomap_ros package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/octomap_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-octomap
Requires:       ros-jade-octomap-msgs
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-tf
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-octomap
BuildRequires:  ros-jade-octomap-msgs
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-tf

%description
octomap_ros provides conversion functions between ROS and OctoMap's native
types. This enables a convenvient use of the octomap package in ROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sat Apr 25 2015 Armin Hornung <HornungA@informatik.uni-freiburg.de> - 0.4.0-1
- Autogenerated by Bloom

* Sat Apr 25 2015 Armin Hornung <HornungA@informatik.uni-freiburg.de> - 0.4.0-0
- Autogenerated by Bloom

