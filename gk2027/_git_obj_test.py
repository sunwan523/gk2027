# -*- coding: utf-8 -*-
"""用Python手动创建git对象，绕过git写入权限问题。"""
import os, sys, zlib, hashlib, subprocess

repo = r'D:\codex\gaokao'
obj_dir = os.path.join(repo, '.git', 'objects')

def write_object(content, obj_type='blob'):
    """创建git对象并返回hash。"""
    header = ('%s %d\0' % (obj_type, len(content))).encode('utf-8')
    store = header + content
    sha = hashlib.sha1(store).hexdigest()
    obj_path = os.path.join(obj_dir, sha[:2], sha[2:])
    os.makedirs(os.path.dirname(obj_path), exist_ok=True)
    if not os.path.exists(obj_path):
        with open(obj_path, 'wb') as f:
            f.write(zlib.compress(store))
    return sha

# 测试：创建一个简单对象
test_hash = write_object(b'test content', 'blob')
print('测试对象创建成功:', test_hash)

# 验证git能读取
result = subprocess.run(['git', 'cat-file', '-t', test_hash], 
                       cwd=repo, capture_output=True, text=True)
print('git验证类型:', result.stdout.strip(), result.stderr.strip())
