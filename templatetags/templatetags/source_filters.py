#coding:utf-8 

from django import template

register = template.Library()  
  
def file_size(size):  
    try:
        size = float(size)
    except:
        return ""
    if(size >= 1024):					#KB
        size /= 1024
        if(size >= 1024):				#MB
            size /= 1024
            if(size >= 1024):			#GB
                size /= 1024
                if(size >= 1024):		#TB
                    size /= 1024
                    return str("%.2f" %size) + "TB"
                return str("%.2f" %size) + "GB"
            return str("%.1f" %size) + "MB"
        return str("%.0f" %size) + "KB"
    return str("%.0f" %size) + "byte"

register.filter('file_size', file_size)
