from scrapy.pipelines.images import ImagesPipeline
from slugify import slugify

class CustomImagesPipeline(ImagesPipeline):
    
    def file_path(self, request, response=None, info=None, *, item=None):
        file_name=slugify(item['title'], max_length=200)
        
        return f'full/{file_name}.jpg'
