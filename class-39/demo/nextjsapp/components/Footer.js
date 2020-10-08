import Link from 'next/link'

export default function Footer(props){
    return (
        <>
            <ul>
                {props.users.map( (person) =>
                    <Link key={person.id} href="/user/[id].js" as={`/user/${person.id}` }>
                        <a>{person.first_name} {person.last_name}</a>
                    </Link>
                )}
            </ul>
            <style jsx>{`
                a{
                    margin-right: 5px;
                    color: green;
                }
            `}
            </style>
            <p><small>@copyright ASAC</small></p>
        </>
    );
}


// NextJS Routing
