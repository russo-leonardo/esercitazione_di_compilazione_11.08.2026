import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { observableToBeFn } from 'rxjs/internal/testing/TestScheduler';

export interface Gioco {
  'id': number;
  'nome': string;
  'anno_pub': number;
  'versione': string;
}



@Injectable({
  providedIn: 'root',
})

export class Service {
  private apiurl = 'http://ominous-fishstick-wrgppj4ww747cvvwj-5000.github.dev'
  private http = inject(HttpClient)

getgiochi(): Observable<Gioco[]> {
  return this.http.get<Gioco[]>(`${this.apiurl}/libri`);
}
}
