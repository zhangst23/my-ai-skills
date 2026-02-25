import os
import subprocess
import argparse

def run_cmd(cmd):
    """运行系统命令并返回输出"""
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        return None

def check_wp_cli():
    """检查 WP-CLI 是否安装"""
    return run_cmd("wp --version") is not None

def create_site(site_path, db_name, db_user, db_pass, title):
    """创建单个 WordPress 站点"""
    if not os.path.exists(site_path):
        os.makedirs(site_path)
    
    os.chdir(site_path)
    
    print(f"--- Deploying {title} at {site_path} ---")
    
    # 1. 下载核心文件
    run_cmd("wp core download")
    
    # 2. 创建 wp-config
    run_cmd(f"wp config create --dbname={db_name} --dbuser={db_user} --dbpass={db_pass}")
    
    # 3. 创建数据库
    run_cmd("wp db create")
    
    # 4. 安装 WordPress
    admin_user = "admin"
    admin_pass = "password123"
    admin_email = "admin@example.com"
    site_url = f"http://localhost/{os.path.basename(site_path)}"
    
    run_cmd(f'wp core install --url="{site_url}" --title="{title}" --admin_user="{admin_user}" --admin_password="{admin_pass}" --admin_email="{admin_email}"')
    
    print(f"Site {title} deployed successfully.")

def main():
    parser = argparse.ArgumentParser(description="WordPress Bulk Deployer")
    subparsers = parser.add_subparsers(dest="command")
    
    # Create command
    create_parser = subparsers.add_parser("create")
    create_parser.add_argument("--count", type=int, default=1, help="Number of sites to create")
    create_parser.add_argument("--prefix", type=str, required=True, help="Prefix for site directories and DB names")
    create_parser.add_argument("--db-user", type=str, required=True)
    create_parser.add_argument("--db-pass", type=str, required=True)
    
    args = parser.parse_args()
    
    if not check_wp_cli():
        print("Error: WP-CLI not found. Please install it first.")
        return

    if args.command == "create":
        base_dir = os.getcwd()
        for i in range(1, args.count + 1):
            site_name = f"{args.prefix}_{i}"
            site_path = os.path.join(base_dir, site_name)
            create_site(site_path, site_name, args.db_user, args.db_pass, f"Site {site_name}")
            os.chdir(base_dir)

if __name__ == "__main__":
    main()
