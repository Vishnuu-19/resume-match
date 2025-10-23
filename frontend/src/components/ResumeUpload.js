import React, { useState } from "react";
import axios from "axios";
import ResultView from "./ResultView";

const ResumeUpload = () => {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!resume || !jobDescription) return alert("Please upload and fill job description!");

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("job_description", jobDescription);

    try {
      setLoading(true);
      const res = await axios.post("http://127.0.0.1:5000/analyze", formData);
      setResult(res.data);
    } catch (error) {
      alert("Error analyzing resume!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-section">
      <h2>Resume Match Analyzer</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept=".pdf,.docx"
          onChange={(e) => setResume(e.target.files[0])}
        />
        <textarea
          placeholder="Paste Job Description here..."
          rows="6"
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
        ></textarea>
        <button type="submit" disabled={loading}>
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>
      </form>

      {result && <ResultView data={result} jobDescription={jobDescription} />}
    </div>
  );
};

export default ResumeUpload;
