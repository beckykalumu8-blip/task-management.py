import { useState,useEffect } from `react`;
import { format } from `date-fns`;

function App() {
    const [currentTime, setCurrentTime] = useState(``);

    useEffect(() => {
        const updateTime =() => {
            constNow = newDate();
            const formattedTime = format(now, `HH:mm:ss`);
            setCurrentTime(formattedTime);
        };

        updateTime();
        const intervalId = setInterval(updateTime, 1000);
        return () => clearInterval(intervalId);
    })

return (
    <div className="class-container">
        <h1>Dynamic Color Clock</h1>
        <p className="clock-display">{currentTime}</p>
    </div>
);
}

export default App;






