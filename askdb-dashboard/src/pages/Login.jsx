
import { SignIn } from "@clerk/clerk-react";

export default function Login() {
    return (
        <div className="min-h-screen bg-[var(--bg-primary)] flex items-center justify-center p-4">
            <SignIn routing="path" path="/login" signUpUrl="/sign-up" />
        </div>
    );
}
