import { useState } from "react";

interface Props {
  onSend: (text: string) => void;
  loading: boolean;
}

const ChatInput = ({ onSend, loading }: Props) => {
  const [text, setText] = useState("");

  const send = () => {
    if (!text.trim()) return;
    onSend(text);
    setText("");
  };

  return (
    <div className="border-t bg-white p-4 flex gap-3">
      <textarea
        className="flex-1 resize-none rounded-xl border p-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
        rows={2}
        placeholder="Ask a Service Desk question..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            send();
          }
        }}
      />

      <button
        onClick={send}
        disabled={loading}
        className="rounded-xl bg-blue-600 px-5 py-2 text-sm font-medium text-white hover:bg-blue-700 disabled:opacity-50"
      >
        {loading ? "…" : "Send"}
      </button>
    </div>
  );
};

export default ChatInput;
