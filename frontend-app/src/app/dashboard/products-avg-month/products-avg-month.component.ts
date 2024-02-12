import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { DashboardService } from '../dashboard.service';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator, PageEvent } from '@angular/material/paginator';
import { skip } from 'rxjs';

@Component({
  selector: 'app-products-avg-month',
  templateUrl: './products-avg-month.component.html',
  styleUrl: './products-avg-month.component.css'
})
export class ProductsAvgMonthComponent implements OnInit{

  data : DataStuct[] = [] ;

  displayedColumns: string[] = ['factory', 'area', 'year','month','avg_month'];
  dataSource! : MatTableDataSource<DataStuct> ;
  
  filtersMsg : string = 'No filter applied'

  @ViewChild(MatPaginator) 
  paginator!: MatPaginator;

  length = 0;
  pageSize = 10;
  pageIndex = 0;
  pageEvent!: PageEvent;
  
  //FILTERS
  factory? : string
  area? : string
  year?:number
  month?:number
  day?:number

  constructor(private dashboard_service: DashboardService) {}

  ngOnInit(): void {}
 

  loadData(skip: number = 0, limit: number = 50, factory?:string,area?:string,year?:number,month?:number,day?:number){
    this.dashboard_service.getProductsAvgMonth(skip,limit,factory,area,year,month).subscribe( (result) => {
      this.data = result;
      this.length = this.data.length;
      this.dataSource = new MatTableDataSource<DataStuct>(this.data);
      this.dataSource.paginator = this.paginator;
 
    } )
  }

  ngAfterViewInit() {

 

    this.dashboard_service.getProductsAvgMonth(0,50,this.factory,this.area,this.year,this.month).subscribe( (result) => {
      this.data = result;
      this.length = this.data.length;
      this.dataSource = new MatTableDataSource<DataStuct>(this.data);
      this.dataSource.paginator = this.paginator;
 
    } )
   
  }

  
  handlePageEvent(e: PageEvent){
    
    if((this.data.length - (e.pageSize * 2))  == ((e.pageIndex ) * e.pageSize)  ){
      console.log("carico altra pagina" + (this.data.length - (e.pageSize *2)) + " " + ((e.pageIndex ) * e.pageSize)  )

      this.dashboard_service.getProductsAvgMonth(e.length,50,this.factory,this.area,this.year,this.month).subscribe( (result) => {
        this.data = this.data.concat(result) ;
        console.log(this.data.length)
        this.dataSource = new MatTableDataSource<DataStuct>(this.data);
        this.dataSource.paginator = this.paginator;
        console.log("paginator:" + this.paginator.pageIndex + " page index:" + e.pageIndex );
        
        this.paginator.pageIndex = e.pageIndex

      } )


    }

  }

  ApplyFilter(){
    console.log('filtro');
    this.loadData(0,50,this.factory,this.area,this.year,this.month,this.day)
  }

}

export interface DataStuct {
  factory: string;
  area: string;
  year: number;
  month: number;
  date : Date;
  avg_month : number ;
}
 
