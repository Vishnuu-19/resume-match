import React, { useState } from "react";
import axios from "axios";

const InterviewChat = ({ firstQuestion }) => {
  const [chat, setChat] = useState([{ sender: "bot", text: firstQuestion }]);
  const [input, setInput] = useState("");

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    setChat([...chat, { sender: "user", text: input }]);
    const formData = new FormData();
    formData.append("user_id", "guest");
    formData.append("answer", input);

    const res = await axios.post("http://127.0.0.1:5000/chat", formData);
    const newMessage = res.data.question || res.data.message;
    setChat((prev) => [...prev, { sender: "bot", text: newMessage }]);
    setInput("");
  };

  return (
    <div className="chat-container">
      <h3>Mock Interview</h3>
      <div className="chat-box">
        {chat.map((msg, i) => (
          <div
            key={i}
            className={msg.sender === "bot" ? "bot-msg" : "user-msg"}
          >
            {msg.text}
          </div>
        ))}
      </div>

      <form onSubmit={sendMessage} className="chat-input">
        <input
          type="text"
          value={input}
          placeholder="Type your answer or 'end session'..."
          onChange={(e) => setInput(e.target.value)}
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
};

export default InterviewChat;
