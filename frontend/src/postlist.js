import  React, { Component } from  'react';
import 'bootstrap/dist/css/bootstrap.min.css';

class postslist extends Component {
  state = {
    postlist: []
  };
    async componentDidMount() {
    try {
      const posts = await fetch('http://127.0.0.1:8000/api/post'); // fetching the data from api, before the page loaded
      const postlist = await posts.json();
      console.log(postslist);
      this.setState({
        postlist
      });
    } catch (e) {
      console.log(e);
    }
  }


  render() {
    return (<div className="container">
  {this.state.postlist.map( post  =>
  <div className="card">
    <h5 className="card-header">{post.title}</h5>
    <div className="card-body">
         <h6 className="card-title">{post.author}</h6>
          <a href={"/"+post.slug} className="btn btn-primary">Read more</a>
    </div>
   </div>
  )}
  </div>
      );
    }
  }
export  default  postslist;
