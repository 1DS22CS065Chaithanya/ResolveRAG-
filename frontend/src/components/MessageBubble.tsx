import { ChatMessage } from "../types/chat";

interface Props {
  message: ChatMessage;
}

const MessageBubble = ({ message }: Props) => {
  const isUser = message.role === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"} mb-4`}>
      <div
        className={`max-w-[75%] rounded-xl px-4 py-3 text-sm whitespace-pre-wrap
        ${isUser
          ? "bg-blue-600 text-white"
          : "bg-gray-100 text-gray-900"
        }`}
      >
        <p>{message.content}</p>

        {message.sources && message.sources.length > 0 && (
          <div className="mt-3 text-xs text-gray-700">
            <p className="font-semibold mb-1">Sources</p>
            <ul className="list-disc list-inside space-y-1">
              {message.sources.map((s, i) => (
                <li key={i}>
                  {s.source} (Page {s.page ?? "N/A"})
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
};

export default MessageBubble;
