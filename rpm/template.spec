Name:           ros-jade-battery-monitor-rmp
Version:        0.0.2
Release:        0%{?dist}
Summary:        ROS battery_monitor_rmp package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/battery_monitor_rmp
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-python-ethernet-rmp
Requires:       ros-jade-rmp-msgs
Requires:       ros-jade-rospy
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-rospy

%description
Monitor for the Segway Batteries

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
* Tue Apr 07 2015 Russell Toris <rctoris@wpi.edu> - 0.0.2-0
- Autogenerated by Bloom

