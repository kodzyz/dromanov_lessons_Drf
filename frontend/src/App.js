import React from 'react'
import AuthorList from './components/AuthorList.js'
import axios from 'axios'
import BookList from './components/BookList.js'
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate, useLocation} from 'react-router-dom'
import AuthorBookList from './components/AuthorBookList.js'

class App extends React.Component {

    constructor(props) {
        super(props)

        this.state = {
            'authors': [],
            'books': []
        }
    }

    componentDidMount() {
        axios
        .get('http://127.0.0.1:8000/api/authors/')
            .then(response => {
                const authors = response.data
                    this.setState(  // меняем состояние компонента
                    {
                        'authors': authors
                    }
                )
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/api/books/')
            .then(response => {
                const books = response.data
                this.setState(
                    {
                        'books': books
                    }
                )
            })
            .catch(error => console.log(error))
    }
//сделаем:
//1. вложенный Route - список книг конкретного автора <Route index
//2. Route - со списком id автора ':authorId'
//3. AuthorBookList - представление для конктерного автора
//4. id получим из глобального состояния this.setState

    render () {
        return (
            <div>
                <BrowserRouter>
                     <nav>
                        <li> <Link to='/'>Authors</Link>< /li>
                        <li> <Link to='/books'> Books </Link> </li>
                     </nav>
                    <Routes>
                        <Route exact path='/' element={<AuthorList authors={this.state.authors} />} />
                        <Route exact path='/books' element={<BookList books={this.state.books} />} />
                        <Route path='/authors'>
                            <Route index element={<AuthorList authors={this.state.authors} />} />
                            <Route path=':authorId' element={<AuthorBookList books={this.state.books} />} />
                        </Route>

                    </Routes>
                 </BrowserRouter>
            </div>
        )
    }
}
export default App;