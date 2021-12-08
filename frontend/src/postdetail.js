import  React, { Component } from  'react';
import 'bootstrap/dist/css/bootstrap.min.css';

class postsdetail extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: []
    };
  }

  async componentDidMount() {
    try {
    const { match: { params } } = this.props
    const url = await fetch(`http://127.0.0.1:8000/api/post/${params.slug}/`)
    const data = await url.json()
    console.log(data)
          this.setState({
            data: data
          });
      }
          catch (e) {
            console.log(e);
          }
  }

render() {
//const { data } = this.state;
      return (<div className="container">
  {this.state.data.map( post  =>
  <div className="card" key={post.slug}>
      <h5 className="card-header">{post.title}</h5>
         <div className="card-body">
             <h6 className="card-title">{post.author}</h6>
             <p className="card-text">{post.content}</p>
         </div>
  </div>
 )}
 </div>
     );
   }
}

export  default  postsdetail;
