import { useState } from "react";
import { queryRag } from "../api/ragApi";
import { ChatMessage } from "../types/chat";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";

const Chat = () => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async (question: string) => {
    const userMsg: ChatMessage = {
      role: "user",
      content: question,
    };

    setMessages((prev) => [...prev, userMsg]);
    setLoading(true);

    try {
      const res = await queryRag(question);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: res.answer,
          sources: res.sources,
        },
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Something went wrong. Please try again.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex h-screen flex-col bg-gray-50">
      <header className="border-b bg-white px-6 py-4 text-lg font-semibold">
        Service Desk AI Assistant
      </header>

      <main className="flex-1 overflow-y-auto px-6 py-6">
        {messages.map((msg, i) => (
          <MessageBubble key={i} message={msg} />
        ))}

        {loading && (
          <MessageBubble
            message={{
              role: "assistant",
              content: "Thinking...",
            }}
          />
        )}
      </main>

      <ChatInput onSend={sendMessage} loading={loading} />
    </div>
  );
};

export default Chat;
