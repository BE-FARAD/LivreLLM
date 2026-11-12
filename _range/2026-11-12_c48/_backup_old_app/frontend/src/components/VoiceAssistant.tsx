import { LiveKitRoom, RoomAudioRenderer, ControlBar, BarVisualizer, useTracks } from "@livekit/components-react";
import "@livekit/components-styles";
import { Track } from "livekit-client";
import { useEffect, useState } from "react";

function VoiceAssistantContent() {
    const tracks = useTracks([Track.Source.Microphone]);
    const micTrack = tracks.find(t => t.source === Track.Source.Microphone);

    return (
        <div className="flex flex-col items-center justify-center h-full text-white">
            <h2 className="text-2xl mb-4">Assistant LivreLLM</h2>
            <div className="h-32 w-full flex items-center justify-center">
                {micTrack && (
                    <BarVisualizer
                        state="listening"
                        barCount={7}
                        trackRef={micTrack}
                        style={{ height: "100px", width: "200px" }}
                    />
                )}
            </div>
            <p className="mt-4 text-gray-400">Parlez pour interagir avec vos livres</p>
        </div>
    );
}

export default function VoiceAssistant() {
    const [token, setToken] = useState("");
    const [url, setUrl] = useState("");

    useEffect(() => {
        async function getToken() {
            try {
                const resp = await fetch("http://localhost:8000/livekit/token");
                const data = await resp.json();
                setToken(data.token);
                setUrl(data.url);
            } catch (e) {
                console.error("Failed to get token", e);
            }
        }
        getToken();
    }, []);

    if (!token) {
        return (
            <div className="flex items-center justify-center p-4 bg-gray-100 rounded-lg">
                <p>Chargement de l'assistant vocal...</p>
            </div>
        );
    }

    return (
        <div className="voice-assistant-container h-[500px] w-full bg-gray-900 rounded-xl overflow-hidden relative">
            <LiveKitRoom
                video={false}
                audio={true}
                token={token}
                serverUrl={url}
                data-lk-theme="default"
                style={{ height: "100%" }}
            >
                <VoiceAssistantContent />
                <RoomAudioRenderer />
                <ControlBar />
            </LiveKitRoom>
        </div>
    );
}
