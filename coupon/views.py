from django.shortcuts import render
from django.http import HttpResponse
import json

def coupon(request):
    if 'coupon_code' in request.GET:  # request.GET(?以降)に'coupon'が存在する場合
        coupon_code = request.GET['coupon_code']
        if coupon_code == '0001':
            benefit = '1000円引きクーポン！'
            deadline = '2019/10/31'
            message = ''
        elif coupon_code == '0002':
            benefit = '10%引きクーポン！'
            deadline = '2019/11/30'
            message = ''
        else:
            benefit = 'NA'
            deadline = 'NA'
            message = '利用可能なクーポンが見つかりません'
        
        params = {
            'coupon_code': coupon_code,
            'coupon_benefit': benefit,
            'coupon_deadline': deadline,
            'message': message
        }
        #return render(request, 'coupon/index.html', params)

        #json形式の文字列を生成
        json_str = json.dumps(params, ensure_ascii=False, indent=2)
        return HttpResponse(json_str)
        
    else:
        return HttpResponse('Error:Not found coupon code!')
