import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { DashboardService } from '../dashboard.service';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator, PageEvent } from '@angular/material/paginator';

@Component({
  selector: 'app-products-day',
  templateUrl: './products-day.component.html',
  styleUrl: './products-day.component.css'
})
export class ProductsDayComponent implements OnInit{

  data : DataStuct[] = [] ;

  displayedColumns: string[] = ['factory', 'area', 'year','month','day','products_day'];
  dataSource! : MatTableDataSource<DataStuct> ;
  
  filtersMsg : string = 'No filter applied'

  @ViewChild(MatPaginator) 
  paginator!: MatPaginator;

  length = 0;
  pageSize = 10;
  pageIndex = 0;
  pageEvent!: PageEvent;
  
  constructor(private dashboard_service: DashboardService) {}

  ngOnInit(): void {}
 

  ngAfterViewInit() {
    this.dashboard_service.getProductsDay().subscribe( (result) => {
      this.data = result;
      this.length = this.data.length;
      this.dataSource = new MatTableDataSource<DataStuct>(this.data);
      this.dataSource.paginator = this.paginator;
 
    } )
   
  }

  
  handlePageEvent(e: PageEvent){
    
    if((this.data.length - (e.pageSize * 2))  == ((e.pageIndex ) * e.pageSize)  ){
      console.log("carico altra pagina" + (this.data.length - (e.pageSize *2)) + " " + ((e.pageIndex ) * e.pageSize)  )
      this.dashboard_service.getProductsDay(e.length,50).subscribe( (result) => {
        this.data = this.data.concat(result) ;
        console.log(this.data.length)
        this.dataSource = new MatTableDataSource<DataStuct>(this.data);
        this.dataSource.paginator = this.paginator;
        console.log("paginator:" + this.paginator.pageIndex + " page index:" + e.pageIndex );
        
        this.paginator.pageIndex = e.pageIndex

      } )


    }

  }

}

export interface DataStuct {
  factory: string;
  area: string;
  year: number;
  month: number;
  day: number;
  date : Date;
  products_day : number ;
}
 
