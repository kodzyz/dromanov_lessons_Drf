// 2:01 ошибка в режиме инкогнито

import React from 'react'
import AuthorList from './components/AuthorList.js'
import axios from 'axios'
import BookList from './components/BookList.js'
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate, useLocation} from 'react-router-dom'
import AuthorBookList from './components/AuthorBookList.js'
import LoginForm from './components/LoginForm.js'

const NotFound = () => {
    var {pathname} = useLocation() // инфо о странице

    return (
        <div>
            Page "{pathname}" not found
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            'authors': [],
            'books': [],
            'token': ''
        }
    }

    obtainAuthToken(login, password) {
        axios
            .post('http://127.0.0.1:8000/api-auth-token/', {
                'username': login,
                'password': password
            })
                //ответ
            .then(response => {
                const token = response.data.token // получили token
                console.log('token:', token)
                localStorage.setItem('token', token) // сохранили token
                this.setState({
                    'token': token
                }, this.getData) // getData вызываем вторым параметром и в неявном виде
            })
            .catch(error => console.log(error))
    }

    // проверка авторизации
    isAuth(){
        return !!this.state.token  // конвертируем в boolean
    }

    componentDidMount(){
        let token = localStorage.getItem('token') // востанавливаем token из хранилища
        this.setState({
            'token': token
        }, this.getData)
    }

    // формирование заголовков
    getHeaders(){
        if(this.isAuth()){
            return {
                'Authorization': 'Token ' + this.state.token
            }
        }
        return {}
    }

    getData() {
        let headers = this.getHeaders()

        axios
            .get('http://127.0.0.1:8000/api/authors/', {headers}) // {'headers': headers}
            .then(response => {
                const authors = response.data
                    this.setState({
                        'authors': authors
                    })
            })
            .catch(error => {
                console.log(error)
                this.setState({ 'authors': [] }) // очищаем список после logout
            })
        axios
            .get('http://127.0.0.1:8000/api/books/', {headers})
            .then(response => {
                const books = response.data
                this.setState(
                    {
                        'books': books
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({ 'books': [] })
            })
    }

    logOut() {
        localStorage.setItem('token', '') // пустая строка - загашенный токен
        this.setState({
            'token': ''
        }, this.getData) // перегружаем данные
    }

    render () {
        return (
            <div>
                <BrowserRouter>
                     <nav>
                        <li> <Link to='/'>Authors</Link>< /li>
                        <li> <Link to='/books'> Books </Link> </li>
                        <li> {this.isAuth() ? <button onClick={() => this.logOut()} > logout </button> : <Link to='/login'> login </Link>} </li>
                     </nav>
                    <Routes>
                    <Route exact path='/' element={<Navigate to='/authors' />} />
                        <Route exact path='/books' element={<BookList books={this.state.books} authors={this.state.authors} />} />
                        <Route exact path='/login' element={<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)} />} />

                        <Route path='/authors'>
                            <Route index element={<AuthorList authors={this.state.authors} />} />
                            <Route path=':authorId' element={<AuthorBookList books={this.state.books} />} />
                        </Route>
                            <Route path='*' element={<NotFound />} />
                    </Routes>
                 </BrowserRouter>
            </div>
        )
    }
}
export default App;