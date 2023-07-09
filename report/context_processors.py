



from .models import Category
from .models import Publisher
import math

def getPublisherCategory(request):

    cat_count = Category.objects.all().count()
    pub_count = Publisher.objects.all().count()
    cat_count1 = int(cat_count//2)
    pub_count1 = int(pub_count // 2)
    all_categories1 = Category.objects.all()[0:cat_count1]
    all_categories2 = Category.objects.all()[cat_count1:]
    all_publishers1 = Publisher.objects.all()[0:pub_count1]
    all_publishers2 = Publisher.objects.all()[pub_count1:]

    return {
        'categories1': all_categories1,
        'categories2': all_categories2,
        'publishers1':all_publishers1,
        'publishers2': all_publishers2,

    }