import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  private apiUrl = 'http://127.0.0.1:8000'

  constructor(private http: HttpClient) {}

  getProductsDay(skip: number = 0, limit: number = 50, factory?:string,area?:string,year?:number,month?:number,day?:number ): Observable<any> {

    let params = '';

    if (factory!=undefined) {
      params+='&factory='+factory
    }
    if (area!=undefined) {
      params+='&area='+area
    }
    if (year != undefined) {
      params+='&year='+year
    }
    if (month != undefined) {
      params+='&month='+month
    }
    if (day != undefined) {
      params+='&day='+day
    }

  

    return this.http.get<any>(this.apiUrl+'/products_day_count?skip='+ skip +'&limit=' + limit +params )
  }

}
