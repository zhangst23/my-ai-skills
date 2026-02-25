---
name: "wordpress-bulk-deploy"
description: "自动化批量部署 WordPress 站点。当用户需要批量创建多个网站、安装主题、配置插件或设置初始内容时调用此技能。"
metadata:
  version: 1.0.0
---

# WordPress 批量建站技能

该技能通过自动化脚本和 WP-CLI（WordPress 命令行接口）实现站点的批量快速部署。

## 核心功能

1. **一键安装**：批量下载并配置 WordPress 核心文件。
2. **自动化配置**：自动设置数据库连接、站点标题、管理员账户。
3. **插件/主题批量化**：统一安装指定的插件集和主题。
4. **初始内容生成**：支持批量创建页面、文章或分类。

## 依赖要求

在使用该技能前，请确保系统已安装：
- **WP-CLI**: 核心驱动工具。
- **PHP**: 运行 WordPress 的基础。
- **MySQL/MariaDB**: 数据库支持。

## 常用指令示例

### 1. 批量创建站点
```bash
python .agents/skills/wordpress-bulk-deploy/scripts/wp_bulk_deploy.py create --count 5 --prefix "mysite" --db-user "root" --db-pass "password"
```

### 2. 统一安装插件
```bash
# 为所有以 "mysite" 开头的站点安装插件
python .agents/skills/wordpress-bulk-deploy/scripts/wp_bulk_deploy.py install-plugins --prefix "mysite" --plugins "seo-by-rank-math,contact-form-7"
```

### 3. 设置初始内容
```bash
python .agents/skills/wordpress-bulk-deploy/scripts/wp_bulk_deploy.py setup-content --prefix "mysite" --pages "About,Services,Contact"
```

## 注意事项

- **环境检查**：运行前会检查 WP-CLI 是否可用。
- **安全性**：建议在受控的服务器环境或 Docker 容器中运行。
- **性能**：批量操作时请确保服务器资源充足。
