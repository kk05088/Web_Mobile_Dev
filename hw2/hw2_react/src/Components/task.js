export default function Task({task, index}){
    return <div>{`Task ${index+1}: ${task.title}`}</div>
}