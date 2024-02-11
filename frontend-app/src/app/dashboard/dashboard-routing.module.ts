import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard.component';
import { ProductsDayComponent } from './products-day/products-day.component';

const routes: Routes = [
  { 
    path: '', 
    component: DashboardComponent,
    children: [
      {
        path: 'products-day', component : ProductsDayComponent
      }
    ] 
  } 
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DashboardRoutingModule { }
