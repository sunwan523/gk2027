# -*- coding: utf-8 -*-
"""用Python创建所有git对象，然后用git提交。"""
import os, sys, zlib, hashlib, subprocess

repo = r'D:\codex\gaokao'
obj_dir = os.path.join(repo, '.git', 'objects')
target_dir = os.path.join(repo, 'gk2027')

def write_object(content, obj_type='blob'):
    header = ('%s %d\0' % (obj_type, len(content))).encode('utf-8')
    store = header + content
    sha = hashlib.sha1(store).hexdigest()
    obj_path = os.path.join(obj_dir, sha[:2], sha[2:])
    os.makedirs(os.path.dirname(obj_path), exist_ok=True)
    if not os.path.exists(obj_path):
        with open(obj_path, 'wb') as f:
            f.write(zlib.compress(store))
    return sha

def get_file_mode(path):
    if os.path.isdir(path):
        return '40000'
    elif os.access(path, os.X_OK):
        return '100755'
    else:
        return '100644'

# 收集所有文件（排除__pycache__、.pyc、output目录、数据库文件）
exclude_dirs = {'__pycache__', '.git', 'output', 'data'}
exclude_exts = {'.pyc', '.db', '.pdf'}
files = []
for root, dirs, filenames in os.walk(target_dir):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for fn in filenames:
        ext = os.path.splitext(fn)[1].lower()
        if ext in exclude_exts:
            continue
        full = os.path.join(root, fn)
        rel = os.path.relpath(full, repo).replace('\\', '/')
        files.append((full, rel))

print('共收集 %d 个文件' % len(files))

# 为每个文件创建blob对象
blobs = []
for full, rel in files:
    with open(full, 'rb') as f:
        content = f.read()
    sha = write_object(content, 'blob')
    mode = get_file_mode(full)
    blobs.append((mode, sha, rel))
    print('  blob: %s %s' % (sha[:8], rel))

# 用git update-index添加所有文件
print()
print('添加到git索引...')
for mode, sha, rel in blobs:
    result = subprocess.run(
        ['git', 'update-index', '--add', '--cacheinfo', mode, sha, rel],
        cwd=repo, capture_output=True, text=True
    )
    if result.returncode != 0:
        print('  失败: %s - %s' % (rel, result.stderr.strip()))

print('索引添加完成')
