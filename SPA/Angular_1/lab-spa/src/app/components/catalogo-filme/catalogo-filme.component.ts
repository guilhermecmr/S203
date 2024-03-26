import { Component } from '@angular/core';
import { FilmeService } from 'src/app/services/filme.service';
import { IFilme } from 'src/app/models/i-filme';

interface OnInit {
  ngOnInit(): void
}

@Component({
  selector: 'app-catalogo-filme',
  templateUrl: './catalogo-filme.component.html',
  styleUrls: ['./catalogo-filme.component.scss']
})

export class CatalogoFilmeComponent implements OnInit {

  books : IFilme[] = [];
  constructor( private service: FilmeService ) { }

  ngOnInit(): void {
    this.books = [
    {id:3, title:'Burning', genre:'Drama'},
    {id:4, title:'Nosferatu', genre:'Horror'},
    {id:5, title:'The Thing', genre:'Science Fiction'},
    ];
    for (let b of this.books) {
      console.log( b.id );
      console.log( b.title );
      console.log( b.genre );
    }
  }
}
