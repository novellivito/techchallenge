import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment' 


@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  private apiUrl = environment.apiUrl

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

  

    return this.http.get<any>(this.apiUrl+'/products_day?skip='+ skip +'&limit=' + limit + params )
  }

  getProductsAvgMonth(skip: number = 0, limit: number = 50, factory?:string,area?:string,year?:number,month?:number): Observable<any> {

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


  

    return this.http.get<any>(this.apiUrl+'/products_avg_month?skip='+ skip +'&limit=' + limit + params )
  }

  getProductsAvgYear(skip: number = 0, limit: number = 50, factory?:string,area?:string,year?:number): Observable<any> {

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
    


  

    return this.http.get<any>(this.apiUrl+'/products_avg_year?skip='+ skip +'&limit=' + limit + params )
  }


}
