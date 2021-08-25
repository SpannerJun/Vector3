# coding: utf-8

Information = {
    'version': '1.0.1',
    'name': 'Vector3',
    'description': 'Can compute Vector3 in XRmaker',
    'author': [
        'Spanner_Jun'
    ],
    'link': 'https://github.com/SpannerJun/Vector3'
}


# 向量加法
def vand(v0, v1):
    v0[0] += v1[0]
    v0[1] += v1[1]
    v0[2] += v1[2]
    return v0


# 向量求模
def vectormag(v0):
    a = v0[0] + v0[1] + v0[2]
    a = a ** 0.5
    return a


# 向量点乘
def vpoint(v0, v1):
    v0[0] *= v1[0]
    v0[1] *= v1[1]
    v0[3] *= v1[2]


# 两点距离
def distance(v0, v1):
    x = v0[0] - v1[0]
    y = v0[1] - v1[1]
    z = v0[2] - v1[2]
    a = x + y + z
    a = a ** 0.5
    return a


# 向量减法
def vdel(v0, v1):
    v0[0] -= v1[0]
    v0[1] -= v1[1]
    v0[2] -= v1[2]
    return v0
