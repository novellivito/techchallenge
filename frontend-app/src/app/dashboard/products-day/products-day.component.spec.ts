import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProductsDayComponent } from './products-day.component';

describe('ProductsDayComponent', () => {
  let component: ProductsDayComponent;
  let fixture: ComponentFixture<ProductsDayComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ProductsDayComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ProductsDayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
