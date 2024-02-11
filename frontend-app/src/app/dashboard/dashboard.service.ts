import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  private apiUrl = 'http://127.0.0.1:8000'

  constructor(private http: HttpClient) {}

  getProductsDay(skip: number = 0, limit: number = 50): Observable<any> {

    return this.http.get<any>(this.apiUrl+'/products_day_count?skip='+ skip +'&limit=' + limit )
  }

}
