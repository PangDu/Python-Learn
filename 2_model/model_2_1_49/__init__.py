from . import projectOne,projectTwo
#获得projectOne和projectTwo中的成员列表字典
membs_p1 = { name:getattr(projectOne,name)
            for name in projectOne.__all__ if hasattr(projectOne,name)
            }

membs_p2 = { name:getattr(projectTwo,name)
            for name in projectTwo.__all__ if hasattr(projectTwo,name)
            }

#更新当前模块的名称空间列表
cur_dict = globals()
cur_dict.update(membs_p1)
cur_dict.update(membs_p2)

#合并__all__属性的内容
__all__ = projectOne.__all__ + projectTwo.__all__
