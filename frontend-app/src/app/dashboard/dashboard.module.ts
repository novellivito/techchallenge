import { NgModule,AfterViewInit, Component, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DashboardRoutingModule } from './dashboard-routing.module';
import { DashboardComponent } from './dashboard.component';

import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatSidenavModule} from '@angular/material/sidenav';
import {RouterOutlet } from '@angular/router';
import {MatListModule} from '@angular/material/list';
import {ProductsDayComponent } from './products-day/products-day.component';
import {HttpClientModule } from '@angular/common/http';
import {MatPaginatorModule} from '@angular/material/paginator';
import {MatTableModule} from '@angular/material/table';
import {MatInputModule} from '@angular/material/input';
import { FormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    DashboardComponent,
    ProductsDayComponent
  ],
  imports: [
    CommonModule,
    DashboardRoutingModule,
    MatToolbarModule, 
    MatButtonModule, 
    MatIconModule, 
    MatSidenavModule,
    RouterOutlet,
    MatListModule,
    HttpClientModule,
    MatTableModule, 
    MatPaginatorModule,
    MatInputModule,
    FormsModule

  ]
})
export class DashboardModule { }
