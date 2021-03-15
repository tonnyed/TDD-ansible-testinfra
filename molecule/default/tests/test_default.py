"""Role testing files using testinfra."""

def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"

def test_nginx_installed(host):
    nginx_package_name = "nginx"
    nginx_package = host.package(nginx_package_name)
    assert nginx_package.is_installed

def test_firewalld_installed(host):
    firewalld_package = host.package("firewalld")
    assert firewalld_package.is_installed

def test_nginx_is_version(host):
    nginx = host.package("nginx")
    assert nginx.version.startswith("1.16.1")

# def test_nginx_running(host):
#     nginx_service = host.service("firewalld")
#     assert nginx_service.is_running

def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled

def test_firewalld_running_and_enabled(host):
    firewalld = host.service("firewalld")
    assert firewalld.is_running
    assert firewalld.is_enabled