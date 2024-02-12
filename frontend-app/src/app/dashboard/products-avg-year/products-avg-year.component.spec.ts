import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ProductsAvgYearComponent } from './products-avg-year.component';

describe('ProductsDayComponent', () => {
  let component: ProductsAvgYearComponent;
  let fixture: ComponentFixture<ProductsAvgYearComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ProductsAvgYearComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ProductsAvgYearComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
