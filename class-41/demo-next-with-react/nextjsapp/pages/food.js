import styles from '../static/css/styles.module.css'
import Header from '../components/Header'
import Footer from '../components/Footer'
import App from '../components/App'

export default function Food(props){
  return (
    <div className={styles.hello}>
        <Header />
        <App />
        <Footer users={props.users}/>
    </div>
  )
}

export async function getServerSideProps(){
    // Call api here
    // Add data to props
    const res = await fetch('https://reqres.in/api/users');
    const dataObj = await res.json();
    console.log(dataObj);
    return { props: {users: dataObj.data} };
}
