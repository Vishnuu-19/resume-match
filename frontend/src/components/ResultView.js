import React, { useState } from "react";
import axios from "axios";
import InterviewChat from "./InterviewChat";

const ResultView = ({ data, jobDescription }) => {
  const [startInterview, setStartInterview] = useState(false);
  const [firstQuestion, setFirstQuestion] = useState("");

  const handleStartInterview = async () => {
    const formData = new FormData();
    formData.append("user_id", "guest");
    formData.append("job_description", jobDescription);

    const res = await axios.post("http://127.0.0.1:5000/start_interview", formData);
    setFirstQuestion(res.data.question);
    setStartInterview(true);
  };

  if (startInterview) {
    return <InterviewChat firstQuestion={firstQuestion} />;
  }

  return (
    <div className="result-section">
      <h3>Match Score: {data.match_score}%</h3>
      <ul>
        {data.suggestions.map((s, i) => (
          <li key={i}>{s}</li>
        ))}
      </ul>

      {data.match_score >= 80 && (
        <button onClick={handleStartInterview}>Start Mock Interview</button>
      )}
    </div>
  );
};

export default ResultView;
