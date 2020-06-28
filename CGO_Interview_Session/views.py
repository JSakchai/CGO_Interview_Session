from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def solution(self,X,A):
    Searchvalue =0
    for time in range(len(A)):
        print(time)
        if A[time] <= X:
            Searchvalue = A[time]
        if Searchvalue == X:
            return HttpResponse(time)

    return HttpResponse(-1)
