import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ProductsAvgMonthComponent } from './products-avg-month.component';

describe('ProductsDayComponent', () => {
  let component: ProductsAvgMonthComponent;
  let fixture: ComponentFixture<ProductsAvgMonthComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ProductsAvgMonthComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ProductsAvgMonthComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
