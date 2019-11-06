from django.shortcuts import render,redirect
from django.http import HttpResponse
from TestModel.models import Test,Contact,Dic,user1
import json
def bing(request):
    begintime=request.POST.get('begin', None)
    endtime=request.POST.get('end', None)
    time1=''
    time2=''
    if request.POST:
        time1=certaintime(begintime)
        time2=certaintime(endtime)

    response = Dic.objects.all()
    srtotime = 0
    swtotime = 0
    sztotime = 0
    totimeelse=0

    srintime=0
    swintime=0
    szintime=0
    intimeelse=0

    srovertime = 0
    swovertime = 0
    szovertime = 0
    overtimeelse=0


    for data in response:
        if ((data.OVERTIME_ARCHIVE_NUM == '-')and(data.INTIME_ARCHIVE_NUM == '-')and(data.testtime<=time2)and(data.testtime>=time1)):
            if (data.EVENT_TYPE_NAME == '市容环卫'):
                srtotime = srtotime + 1
            elif (data.EVENT_TYPE_NAME == '环保水务'):
                swtotime = swtotime + 1
            elif (data.EVENT_TYPE_NAME == '市政设施'):
                sztotime = sztotime + 1
            else:
                totimeelse =totimeelse+1

        if ((data.INTIME_ARCHIVE_NUM == '1')and(data.testtime<=time2)and(data.testtime>=time1)):
            if (data.EVENT_TYPE_NAME == '市容环卫'):
                srintime = srintime + 1
            elif (data.EVENT_TYPE_NAME == '环保水务'):
                swintime = swintime + 1
            elif (data.EVENT_TYPE_NAME == '市政设施'):
                szintime = szintime + 1
            else:
                intimeelse =intimeelse+1

        if ((data.OVERTIME_ARCHIVE_NUM == '1')and(data.testtime<=time2)and(data.testtime>=time1)):
            if (data.EVENT_TYPE_NAME == '市容环卫'):
                srovertime = srovertime + 1
            elif (data.EVENT_TYPE_NAME == '环保水务'):
                swovertime = swovertime + 1
            elif (data.EVENT_TYPE_NAME == '市政设施'):
                szovertime = szovertime + 1
            else:
                overtimeelse = overtimeelse + 1
    
    list =[srtotime, swtotime, sztotime, totimeelse, srintime, swintime, szintime, intimeelse, srovertime,swovertime,szovertime, overtimeelse]
    #list =[1,2,3,4,5,6,7,8,9,10,11,12]
    return render(request, 'first.html', {
        'List': json.dumps(list),'begintime':time1,'endtime':time2})
def gun(request):
    response = Dic.objects.order_by('testtime')[0:3]
    b=[]
    for a in response:
        b.append(a)
        
    return render(request, 'runing.html', {'one':b})
def certaintime(ttime):
    i = 0
    day = ''
    month = ''
    year = ''
    for a in ttime:
        if ((i == 0) and (a != '/')):
            month = month + a
        if ((i == 1) and (a != '/')):
            day = day + a
        if ((i == 2) and (a != '/')):
            year = year + a
        if (a == '/'):
            i = i + 1
    if(len(day)==1):
        day='0'+day
    if(len(month)==1):
        month='0'+month
    ctime = year + month + day + '000000'
    return ctime
def hotpot(request):
    ph=0
    ll=0
    bl=0
    tk=0
    sh=0
    ml=0
    jl=0
    sx=0
    jg=0
    sj=0
    tt=0
    tx=0
    zk=0
    nb=0
    ps=0
    lh=0
    hp=0
    kz=0
    lk=0
    lt=0
    xx=0
    js=0
    st=0

    response = Dic.objects.all()
    
    for data in response:
        if (data.COMMUNITY_NAME == '坪环社区'):
            ph=ph+1
        elif (data.COMMUNITY_NAME == '六联社区'):
            ll=ll+1
        elif (data.COMMUNITY_NAME == '碧岭社区'):
            bl=bl+1
        elif (data.COMMUNITY_NAME == '汤坑社区'):
            tk=tk+1
        elif (data.COMMUNITY_NAME == '沙湖社区'):
            sh=sh+1
        elif (data.COMMUNITY_NAME == '马峦社区'):
            ml=ml+1
        elif (data.COMMUNITY_NAME == '江岭社区'):
            jl=jl+1
        elif (data.COMMUNITY_NAME == '沙坣社区'):
            sx=sx+1
        elif (data.COMMUNITY_NAME == '金龟社区'):
            jg=jg+1
        elif (data.COMMUNITY_NAME == '石井社区'):
            sj=sj+1
        elif (data.COMMUNITY_NAME == '田头社区'):
            tt=tt+1
        elif (data.COMMUNITY_NAME == '田心社区'):
            tx=tx+1
        elif (data.COMMUNITY_NAME == '竹坑社区'):
            zk=zk+1
        elif (data.COMMUNITY_NAME == '南布社区'):
            nb=nb+1
        elif (data.COMMUNITY_NAME == '坪山社区'):
            ps=ps+1
        elif (data.COMMUNITY_NAME == '六和社区'):
            lh=lh+1
        elif (data.COMMUNITY_NAME == '和平社区'):
            hp=hp+1
        elif (data.COMMUNITY_NAME == '坑梓社区'):
            kz=kz+1
        elif (data.COMMUNITY_NAME == '老坑社区'):
            lk=lk+1
        elif (data.COMMUNITY_NAME == '龙田社区'):
            lt=lt+1
        elif (data.COMMUNITY_NAME == '秀新社区'):
            xx=xx+1
        elif (data.COMMUNITY_NAME == '金沙社区'):
            js=js+1
        elif (data.COMMUNITY_NAME == '沙田社区'):
            st=st+1
        else:
            pass

    list=[ph,ll,bl,tk,sh,ml,jl,sx,jg,sj,tt,tx,zk,nb,ps,lh,hp,kz,lk,lt,xx,js,st]
    return render(request,'hotpowergraph.html', {
        'List2': json.dumps(list),})