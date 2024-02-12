import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard.component';
import { ProductsDayComponent } from './products-day/products-day.component';
import { ProductsAvgMonthComponent } from './products-avg-month/products-avg-month.component';
import { ProductsAvgYearComponent } from './products-avg-year/products-avg-year.component';

const routes: Routes = [
  { 
    path: '', 
    component: DashboardComponent,
    children: [
      {
        path: 'products-day', component : ProductsDayComponent
      } ,
      {
        path: 'products-avg-month', component : ProductsAvgMonthComponent
      },
      {
        path: 'products-avg-year', component : ProductsAvgYearComponent
      }

    ] 
  } 
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DashboardRoutingModule { }
